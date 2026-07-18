import { useEffect, useState } from "react";
import {
  getSatellites,
  getRisk,
  getPrediction,
  getNegotiation,
  getConjunctions,
} from "../services/simulationService";

export default function MissingReport() {
  const [satellites, setSatellites] = useState<any[]>([]);
  const [risk, setRisk] = useState<any>(null);
  const [prediction, setPrediction] = useState<any>(null);
  const [negotiation, setNegotiation] = useState<any>(null);
  const [conjunctions, setConjunctions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [
          satRes,
          riskRes,
          predRes,
          negRes,
          conjRes,
        ] = await Promise.all([
          getSatellites(),
          getRisk(),
          getPrediction(),
          getNegotiation(),
          getConjunctions(),
        ]);

        setSatellites(satRes.data.satellites);
        setRisk(riskRes.data);
        setPrediction(predRes.data);
        setNegotiation(negRes.data.negotiation);
        setConjunctions(conjRes.data.conjunctions);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-[70vh] text-cyan-300 text-2xl">
        Loading Mission Report...
      </div>
    );
  }

  return (
    <div className="space-y-6">

      <div className="rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-6 backdrop-blur-xl">
        <h1 className="text-3xl font-bold text-cyan-300">
          Mission Report
        </h1>

        <p className="text-slate-400 mt-2">
          Live backend mission summary
        </p>
      </div>

      <div className="grid md:grid-cols-3 gap-6">

        <div className="rounded-xl bg-slate-900/60 border border-cyan-500/20 p-6">
          <p className="text-slate-400">Satellites</p>
          <h2 className="text-4xl font-bold text-cyan-300 mt-2">
            {satellites.length}
          </h2>
        </div>

        <div className="rounded-xl bg-slate-900/60 border border-cyan-500/20 p-6">
          <p className="text-slate-400">Conjunctions</p>
          <h2 className="text-4xl font-bold text-yellow-300 mt-2">
            {conjunctions.length}
          </h2>
        </div>

        <div className="rounded-xl bg-slate-900/60 border border-cyan-500/20 p-6">
          <p className="text-slate-400">Collision Probability</p>
          <h2 className="text-4xl font-bold text-red-400 mt-2">
            {(prediction.collision_probability * 100).toFixed(2)}%
          </h2>
        </div>

      </div>

      <div className="grid md:grid-cols-2 gap-6">

        <div className="rounded-xl bg-slate-900/60 border border-cyan-500/20 p-6">

          <h2 className="text-xl font-semibold text-cyan-300 mb-4">
            Negotiation
          </h2>

          <div className="space-y-3">

            <p>
              <span className="text-slate-400">Status :</span>{" "}
              <span className="text-green-400 font-semibold">
                {negotiation.status}
              </span>
            </p>

            <p>
              <span className="text-slate-400">Winner :</span>{" "}
              {negotiation.winner}
            </p>

            <p>
              <span className="text-slate-400">Yielding :</span>{" "}
              {negotiation.yielding_satellite}
            </p>

            <p>
              <span className="text-slate-400">Method :</span>{" "}
              {negotiation.resolution_method}
            </p>

            <p>
              <span className="text-slate-400">Confidence :</span>{" "}
              {(negotiation.confidence * 100).toFixed(0)}%
            </p>

          </div>

        </div>

        <div className="rounded-xl bg-slate-900/60 border border-cyan-500/20 p-6">

          <h2 className="text-xl font-semibold text-cyan-300 mb-4">
            Risk Analysis
          </h2>

          <div className="space-y-3">

            <p>
              <span className="text-slate-400">Risk Level :</span>{" "}
              {risk.risk_level}
            </p>

            <p>
              <span className="text-slate-400">Recommended Action :</span>{" "}
              {risk.recommended_action}
            </p>

            <p>
              <span className="text-slate-400">Negotiation Required :</span>{" "}
              {risk.requires_negotiation ? "YES" : "NO"}
            </p>

            <p className="text-slate-300">
              {risk.notes}
            </p>

          </div>

        </div>

      </div>

      <div className="rounded-xl bg-slate-900/60 border border-cyan-500/20 p-6">

        <h2 className="text-xl font-semibold text-cyan-300 mb-4">
          Mission Summary
        </h2>

        <ul className="space-y-2 text-slate-300">

          <li>✔ {satellites.length} Active Satellites</li>

          <li>✔ {conjunctions.length} Possible Conjunctions</li>

          <li>
            ✔ Collision Probability :
            {" "}
            {(prediction.collision_probability * 100).toFixed(2)}%
          </li>

          <li>
            ✔ Negotiation completed successfully.
          </li>

          <li>
            ✔ Highest priority satellite :
            {" "}
            {negotiation.winner}
          </li>

        </ul>

      </div>

    </div>
  );
}