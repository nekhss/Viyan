import { useEffect, useState } from "react";
import { getConjunctions } from "../services/simulationService";

interface Conjunction {
  satellite1: {
    name: string;
  };
  satellite2: {
    name: string;
  };
  closest_distance_km: number;
  time_to_closest_sec: number;
}

export default function Simulation() {
  const [conjunctions, setConjunctions] = useState<Conjunction[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchConjunctions = async () => {
      try {
        const response = await getConjunctions();
        setConjunctions(response.data.conjunctions);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchConjunctions();
  }, []);

  const filtered = conjunctions.filter(
    (item) =>
      item.satellite1.name.toLowerCase().includes(search.toLowerCase()) ||
      item.satellite2.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6">

      {/* Header */}

      <div className="rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-6 backdrop-blur-xl">

        <div className="flex items-center justify-between">

          <div>
            <h1 className="text-3xl font-bold text-cyan-300">
              Simulation Results
            </h1>

            <p className="mt-2 text-slate-400">
              Live conjunction analysis from backend
            </p>
          </div>

          <div className="rounded-xl bg-cyan-500/10 px-5 py-3">

            <p className="text-sm text-slate-400">
              Total Conjunctions
            </p>

            <h2 className="text-3xl font-bold text-cyan-300">
              {conjunctions.length}
            </h2>

          </div>

        </div>

      </div>

      {/* Search */}

      <div className="rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-4 backdrop-blur-xl">

        <input
          type="text"
          placeholder="Search Satellite..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full rounded-lg border border-cyan-500/20 bg-slate-800 px-4 py-3 text-white outline-none focus:border-cyan-400"
        />

      </div>

      {/* Table */}

      <div className="overflow-hidden rounded-2xl border border-cyan-500/20 bg-slate-900/60 backdrop-blur-xl">

        {loading ? (

          <div className="p-10 text-center text-cyan-300 text-lg">
            Loading Simulation...
          </div>

        ) : (

          <div className="overflow-x-auto">

            <table className="w-full">

              <thead className="bg-slate-800">

                <tr className="text-left text-cyan-300">

                  <th className="px-6 py-4">
                    Satellite 1
                  </th>

                  <th className="px-6 py-4">
                    Satellite 2
                  </th>

                  <th className="px-6 py-4">
                    Closest Distance
                  </th>

                  <th className="px-6 py-4">
                    Time to Closest
                  </th>

                  <th className="px-6 py-4">
                    Status
                  </th>

                </tr>

              </thead>

              <tbody>

                {filtered.map((item, index) => (

                  <tr
                    key={index}
                    className="border-t border-slate-700 hover:bg-slate-800/50 transition"
                  >

                    <td className="px-6 py-4 font-medium">
                      {item.satellite1.name}
                    </td>

                    <td className="px-6 py-4">
                      {item.satellite2.name}
                    </td>

                    <td className="px-6 py-4">

                      <span
                        className={`font-semibold ${
                          item.closest_distance_km < 0.2
                            ? "text-red-400"
                            : item.closest_distance_km < 1
                            ? "text-yellow-300"
                            : "text-green-400"
                        }`}
                      >
                        {item.closest_distance_km.toFixed(3)} km
                      </span>

                    </td>

                    <td className="px-6 py-4">
                      {item.time_to_closest_sec} sec
                    </td>

                    <td className="px-6 py-4">

                      <span
                        className={`rounded-full px-3 py-1 text-sm font-semibold ${
                          item.closest_distance_km < 0.2
                            ? "bg-red-500/20 text-red-400"
                            : item.closest_distance_km < 1
                            ? "bg-yellow-500/20 text-yellow-300"
                            : "bg-green-500/20 text-green-400"
                        }`}
                      >
                        {item.closest_distance_km < 0.2
                          ? "Critical"
                          : item.closest_distance_km < 1
                          ? "Warning"
                          : "Safe"}
                      </span>

                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        )}

      </div>

    </div>
  );
}