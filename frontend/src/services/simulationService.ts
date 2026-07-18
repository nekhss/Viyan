import api from "./api";

export const getSatellites = () =>
  api.get("/simulation/satellites");

export const getConjunctions = () =>
  api.get("/simulation/conjunctions");

export const getRisk = () =>
  api.get("/simulation/risk");

export const getPrediction = () =>
  api.get("/simulation/prediction");

export const getNegotiation = () =>
  api.get("/simulation/negotiation");

export const runSimulation = () =>
  api.post("/simulation/run");