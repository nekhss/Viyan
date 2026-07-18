from fastapi import APIRouter, HTTPException

from simulation.data_loader import load_satellites
from simulation.trajectory import predict_trajectory
from simulation.collision import detect_future_conjunctions
from simulation.features import extract_features
from simulation.risk import assess_risk
from simulation.negotiation import negotiate
from simulation.decision import make_decision
from simulation.ml.predict import predict_collision_probability

router = APIRouter(
    prefix="/simulation",
    tags=["Simulation"],
)


@router.post("/run")
def run_simulation():

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    conjunctions = detect_future_conjunctions(satellites)

    if not conjunctions:
        raise HTTPException(
            status_code=404,
            detail="No conjunctions detected."
        )

    results = []

    for conjunction in conjunctions:

        features = extract_features(conjunction)

        risk = assess_risk(features)

        probability = predict_collision_probability(features)

        negotiation = negotiate(features, risk)

        decision = make_decision(
            features,
            risk,
            negotiation,
        )

        results.append(
            {
                "conjunction": conjunction,
                "features": features,
                "risk": risk,
                "ml_prediction": probability,
                "negotiation": negotiation,
                "decision": decision,
            }
        )

    return {
        "total_conjunctions": len(results),
        "results": results,
    }


@router.get("/satellites")
def get_satellites():

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    return {
        "count": len(satellites),
        "satellites": satellites,
    }


@router.get("/conjunctions")
def get_conjunctions():

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    conjunctions = detect_future_conjunctions(satellites)

    return {
        "count": len(conjunctions),
        "conjunctions": conjunctions,
    }


@router.get("/risk")
def get_risk():

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    conjunctions = detect_future_conjunctions(satellites)

    if not conjunctions:
        raise HTTPException(
            status_code=404,
            detail="No conjunctions detected."
        )

    features = extract_features(conjunctions[0])

    risk = assess_risk(features)

    return risk


@router.get("/prediction")
def get_prediction():

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    conjunctions = detect_future_conjunctions(satellites)

    if not conjunctions:
        raise HTTPException(
            status_code=404,
            detail="No conjunctions detected."
        )

    features = extract_features(conjunctions[0])

    probability = predict_collision_probability(features)

    return {
        "collision_probability": probability
    }


@router.get("/negotiation")
def get_negotiation():

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    conjunctions = detect_future_conjunctions(satellites)

    if not conjunctions:
        raise HTTPException(
            status_code=404,
            detail="No conjunctions detected."
        )

    features = extract_features(conjunctions[0])

    risk = assess_risk(features)

    negotiation = negotiate(features, risk)

    return negotiation


@router.get("/satellite/{name}")
def satellite_status(name: str):

    satellites = load_satellites(
        "stations",
        force_refresh=True,
    )

    search = name.strip().lower()

    satellite = next(
        (
            s
            for s in satellites
            if search in s["name"].strip().lower()
        ),
        None,
    )

    if satellite is None:
        raise HTTPException(
            status_code=404,
            detail="Satellite not found",
        )

    trajectory = predict_trajectory(
        satellite,
        minutes=1,
        step=60,
    )

    current = trajectory[0]

    return {
        "name": satellite["name"],
        "position": current["position"],
        "velocity": current["velocity"],
        "geographic": current["geographic"],
    }