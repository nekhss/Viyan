import earth from "../../assets/space/earth.webp";
import satellite from "../../assets/space/satellite.webp";
import { useEffect, useState } from "react";
import {
  getSatellites,
  getRisk,
  getPrediction,
} from "../../services/simulationService";
export default function OrbitView() {
  const [satellites, setSatellites] = useState<any[]>([]);
  const [risk, setRisk] = useState<any>(null);
  const [prediction, setPrediction] = useState<any>(null);
useEffect(() => {
  const fetchData = async () => {
    try {
      const satelliteResponse = await getSatellites();
      setSatellites(satelliteResponse.data.satellites);

      const riskResponse = await getRisk();
      const predictionResponse = await getPrediction();
      setPrediction(predictionResponse.data);
      setRisk(riskResponse.data);
    } catch (error) {
      console.error(error);
    }
  };

  fetchData();
}, []);
  return (
    <div className="relative h-[760px] overflow-hidden rounded-3xl border border-cyan-500/20 bg-[#071425]/70 backdrop-blur-xl">

      {/* Background Glow */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(34,211,238,0.08),transparent_70%)]" />

      {/* Stars */}
      {[...Array(120)].map((_, i) => (
        <div
          key={i}
          className="absolute rounded-full bg-white opacity-70 animate-pulse"
          style={{
            width: `${Math.random() * 3 + 1}px`,
            height: `${Math.random() * 3 + 1}px`,
            top: `${Math.random() * 100}%`,
            left: `${Math.random() * 100}%`,
            animationDuration: `${2 + Math.random() * 4}s`,
          }}
        />
      ))}

      {/* Title */}
      <div className="absolute left-8 top-8 z-20">
        <h1 className="text-4xl font-bold text-cyan-300">
          Orbital Command Center
        </h1>

        <p className="mt-2 text-slate-400">
          Autonomous Satellite Coordination
        </p>
      </div>

      {/* Orbit Rings */}
      <div className="absolute inset-0 flex items-center justify-center">

        <div className="absolute h-72 w-72 rounded-full border border-cyan-400/20" />

        <div className="absolute h-[470px] w-[470px] rounded-full border border-cyan-400/15" />

        <div className="absolute h-[620px] w-[620px] rounded-full border border-cyan-400/10" />

      </div>

      {/* Earth */}
<div className="absolute left-1/2 top-1/2 z-10 -translate-x-1/2 -translate-y-1/2">

  {/* Glow */}
  <div className="absolute inset-0 scale-150 rounded-full bg-cyan-400/30 blur-3xl animate-pulse"></div>

  <img
    src={earth}
    alt="Earth"
    className="relative h-44 w-44 rounded-full object-cover border-[4px] border-cyan-300
    shadow-[0_0_60px_rgba(34,211,238,0.8)]"
    style={{
        clipPath: "circle(50%)",
    }}
/>

</div>
{/* Communication Beam */}
<div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">

  <div className="h-44 w-[2px] bg-cyan-400/20 relative">

    <div className="absolute top-0 left-0 w-full h-16 bg-cyan-300 animate-pulse shadow-[0_0_20px_#22d3ee]"></div>

  </div>

</div>
      {/* Orbit 1 */}
      <div className="absolute left-1/2 top-1/2 h-72 w-72 -translate-x-1/2 -translate-y-1/2 animate-[spin_18s_linear_infinite]">

        <img
          src={satellite}
          className="absolute left-1/2 top-0 w-12 -translate-x-1/2"
          alt=""
        />

      </div>

      {/* Orbit 2 */}
      <div className="absolute left-1/2 top-1/2 h-[470px] w-[470px] -translate-x-1/2 -translate-y-1/2 animate-[spin_28s_linear_infinite]">

        <img
          src={satellite}
          className="absolute right-0 top-1/2 w-12 -translate-y-1/2"
          alt=""
        />

      </div>

      {/* Orbit 3 */}
      <div className="absolute left-1/2 top-1/2 h-[620px] w-[620px] -translate-x-1/2 -translate-y-1/2 animate-[spin_40s_linear_infinite]">

        <img
          src={satellite}
          className="absolute bottom-0 left-1/2 w-12 -translate-x-1/2"
          alt=""
        />

      </div>

      {/* Reverse Orbit */}
      <div className="absolute left-1/2 top-1/2 h-[470px] w-[470px] -translate-x-1/2 -translate-y-1/2 animate-[spin_32s_linear_infinite_reverse]">

        <img
          src={satellite}
          className="absolute left-0 top-1/2 w-12 -translate-y-1/2"
          alt=""
        />

      </div>
    {/* Live Satellites */}
<div className="absolute right-6 top-28 w-72 rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-4 backdrop-blur-xl">
  <h3 className="mb-3 text-cyan-300 font-semibold">
    Live Satellites
  </h3>

  <div className="max-h-60 overflow-y-auto space-y-2">
    {satellites.map((sat) => (
      <div
        key={sat.name}
        className="rounded-lg bg-slate-800/60 px-3 py-2 text-sm"
      >
        {sat.name}
      </div>
    ))}
  </div>
</div>
      {/* Bottom Stats */}
      <div className="absolute bottom-8 left-1/2 flex w-[90%] -translate-x-1/2 justify-between">

        <div className="rounded-xl border border-cyan-500/20 bg-slate-900/60 px-6 py-4 backdrop-blur-xl">
          <p className="text-sm text-slate-400">Active Satellites</p>
          <h2 className="mt-2 text-3xl font-bold text-cyan-300">
  {satellites.length}
</h2>
        </div>

        <div className="rounded-xl border border-cyan-500/20 bg-slate-900/60 px-6 py-4 backdrop-blur-xl">
         <p className="text-sm text-slate-400">
  Collision Risk
</p>

<h2
  className={`mt-2 text-3xl font-bold ${
    risk?.requires_negotiation
      ? "text-red-400"
      : "text-green-400"
  }`}
>
  {risk?.risk_level ?? "Loading..."}
</h2>
<p className="mt-2 text-xs text-slate-400">
  {risk?.notes}
</p>
        </div>

        <div className="rounded-xl border border-cyan-500/20 bg-slate-900/60 px-6 py-4 backdrop-blur-xl">
          <p className="text-sm text-slate-400">
  Collision Probability
</p>

<h2
  className={`mt-2 text-3xl font-bold ${
    prediction?.collision_probability > 0.7
      ? "text-red-400"
      : prediction?.collision_probability > 0.3
      ? "text-yellow-300"
      : "text-green-400"
  }`}
>
  {prediction
    ? `${(prediction.collision_probability * 100).toFixed(2)}%`
    : "Loading..."}
</h2>
        </div>

        <div className="rounded-xl border border-cyan-500/20 bg-slate-900/60 px-6 py-4 backdrop-blur-xl">
          <p className="text-sm text-slate-400">Mission Health</p>
          <h2 className="mt-2 text-3xl font-bold text-cyan-300">97%</h2>
        </div>

      </div>

    </div>
  );
}