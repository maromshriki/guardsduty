from app.models.swap_request import SwapRequest
from app.models.swap_match import SwapMatch
from app.models.shift import Shift

def try_match(db, new_request: SwapRequest):
    shift = db.get(Shift, new_request.shift_id)

    other = (
        db.query(SwapRequest)
        .join(Shift, SwapRequest.shift_id == Shift.id)
        .filter(
            SwapRequest.status == "open",
            Shift.date == shift.date,
            Shift.start_time == shift.start_time,
            Shift.position_id == shift.position_id,
            Shift.guard_id != shift.guard_id
        )
        .first()
    )

    if other:
        match = SwapMatch(
            shift_a_id=new_request.shift_id,
            shift_b_id=other.shift_id
        )
        new_request.status = "matched"
        other.status = "matched"
        db.add(match)
        db.commit()
        return match

    return None


def execute_swap(db, match: SwapMatch):
    a = db.get(Shift, match.shift_a_id)
    b = db.get(Shift, match.shift_b_id)

    a.guard_id, b.guard_id = b.guard_id, a.guard_id
    db.commit()

