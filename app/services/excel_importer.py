import pandas as pd
from datetime import datetime
from app.models.guard import Guard
from app.models.position import Position
from app.models.shift import Shift
from app.services.normalization import normalize_name
from app.utils.time_utils import parse_time

def import_excel(path: str, db):
    df = pd.read_excel(path, header=[0,1])

    for col_group in range(1, len(df.columns), 2):
        header = df.columns[col_group][0]
        date = datetime.strptime(header.split()[0], "%d/%m/%Y").date()

        time_col = df.columns[col_group - 1]
        guard_col = df.columns[col_group]

        for _, row in df.iterrows():
            position_name = row[0]
            guard_name = row[guard_col]
            time_val = row[time_col]

            if pd.isna(guard_name) or pd.isna(time_val):
                continue

            norm_name = normalize_name(str(guard_name))

            guard = db.query(Guard).filter_by(name_normalized=norm_name).first()
            if not guard:
                guard = Guard(
                    name_original=guard_name,
                    name_normalized=norm_name
                )
                db.add(guard)
                db.flush()

            position = db.query(Position).filter_by(name=position_name).first()
            if not position:
                position = Position(name=position_name)
                db.add(position)
                db.flush()

            shift = Shift(
                date=date,
                start_time=parse_time(time_val),
                guard_id=guard.id,
                position_id=position.id
            )
            db.merge(shift)

    db.commit()

