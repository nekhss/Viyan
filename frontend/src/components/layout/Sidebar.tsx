import {
  Home,
  Orbit,
  FileText,
  Satellite,
  Fuel,
  Radar,
} from "lucide-react";
import { Link, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { getSatellites } from "../../services/simulationService";

export default function Sidebar() {
  const location = useLocation();
  const [satellites, setSatellites] = useState<any[]>([]);

useEffect(() => {
  const fetchSatellites = async () => {
    try {
      const response = await getSatellites();
      setSatellites(response.data.satellites);
    } catch (error) {
      console.error("Failed to fetch satellites:", error);
    }
  };

  fetchSatellites();
}, []);
  const menu = [
    {
      name: "Dashboard",
      path: "/",
      icon: Home,
    },
    {
      name: "Simulation",
      path: "/simulation",
      icon: Orbit,
    },
    {
      name: "Mission Report",
      path: "/report",
      icon: FileText,
    },
  ];

  return (
    <div className="flex h-full flex-col p-5">

      {/* Logo */}
      <div>

        <h1 className="text-3xl font-bold text-cyan-300">
          VIYAN
        </h1>

        <p className="text-xs text-slate-500 mt-1">
          Fleet Command
        </p>

      </div>

      {/* Fleet Status */}

      <div className="mt-8 rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-4">

        <div className="flex items-center gap-2">

          <Satellite className="text-cyan-300" size={20} />

          <h2 className="font-semibold text-cyan-300">
            Fleet
          </h2>

        </div>

      <div className="mt-5 space-y-4 max-h-72 overflow-y-auto">

  {satellites.length === 0 ? (
    <p className="text-center text-sm text-slate-400">
      Loading satellites...
    </p>
  ) : (
    satellites.map((satellite, index) => (
      <div
        key={satellite.name}
        className="rounded-xl bg-slate-800/70 p-3"
      >
        <div className="flex justify-between">
          <span className="text-sm font-medium truncate">
            {satellite.name}
          </span>

          <span
            className={`${
              index % 3 === 0
                ? "text-green-400"
                : index % 3 === 1
                ? "text-yellow-400"
                : "text-red-400"
            }`}
          >
            ●
          </span>
        </div>

        <div className="mt-2 text-xs text-slate-400">
          TLE Line 1
        </div>

        <div className="truncate text-[10px] text-cyan-300">
          {satellite.line1}
        </div>

        <div className="mt-2 text-xs text-slate-400">
          TLE Line 2
        </div>

        <div className="truncate text-[10px] text-white">
          {satellite.line2}
        </div>
      </div>
    ))
  )}

</div>

      </div>

      {/* Navigation */}

      <div className="mt-8">

        <h3 className="mb-3 text-xs uppercase tracking-widest text-slate-500">
          Navigation
        </h3>

        <nav className="space-y-2">

          {menu.map((item) => {
            const Icon = item.icon;

            return (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center gap-3 rounded-xl p-3 transition-all duration-300 ${
                  location.pathname === item.path
                    ? "bg-cyan-500 text-white shadow-lg shadow-cyan-500/20"
                    : "text-slate-300 hover:bg-slate-800"
                }`}
              >
                <Icon size={20} />

                {item.name}

              </Link>
            );
          })}

        </nav>

      </div>

      {/* Bottom */}

      <div className="mt-auto rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-4">

        <div className="flex items-center gap-2">

          <Radar size={18} className="text-cyan-300" />

          <span className="text-cyan-300">
            Radar
          </span>

        </div>

        <div className="mt-4">

          <div className="flex justify-between text-sm">

            <span className="text-slate-400">
              Mission Health
            </span>

            <span className="text-green-400">
              97%
            </span>

          </div>

          <div className="mt-2 h-2 rounded-full bg-slate-700">

            <div className="h-full w-[97%] rounded-full bg-green-400"></div>

          </div>

        </div>

        <div className="mt-4 flex items-center gap-2 text-sm text-slate-400">

          <Fuel size={16} />

          Fuel Stable

        </div>

      </div>

    </div>
  );
}