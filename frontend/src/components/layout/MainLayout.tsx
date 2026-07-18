import Header from "./Header";
import Sidebar from "./Sidebar";
import SpaceBackground from "../background/SpaceBackground";
import { useEffect, useState } from "react";
import { getNegotiation } from "../../services/simulationService";
interface MainLayoutProps {
  children: React.ReactNode;
}

export default function MainLayout({ children }: MainLayoutProps) {
  const [negotiation, setNegotiation] = useState<any>(null);

useEffect(() => {
  const fetchNegotiation = async () => {
    try {
      const response = await getNegotiation();
      setNegotiation(response.data.negotiation);
    } catch (error) {
      console.error(error);
    }
  };

  fetchNegotiation();
}, []);
  return (
    <div className="relative min-h-screen overflow-hidden bg-[#020617] text-white">

      {/* Animated Space Background */}
      <SpaceBackground />

      {/* Top Glow */}
      <div className="pointer-events-none absolute -top-40 left-1/2 h-96 w-96 -translate-x-1/2 rounded-full bg-cyan-500/20 blur-[140px]" />

      {/* Bottom Glow */}
      <div className="pointer-events-none absolute bottom-0 right-0 h-72 w-72 rounded-full bg-blue-600/10 blur-[120px]" />

      {/* Header */}
      <Header />

      {/* Main Area */}
      <div className="relative flex h-[calc(100vh-64px)]">

        {/* LEFT SIDEBAR */}
        <aside className="w-72 border-r border-cyan-500/10 bg-white/5 backdrop-blur-xl">
          <Sidebar />
        </aside>

        {/* CENTER */}
        <main className="flex-1 overflow-auto p-6">
          {children}
        </main>

        {/* RIGHT PANEL */}
        <aside className="w-96 border-l border-cyan-500/10 bg-white/5 backdrop-blur-xl">

          <div className="p-6">

            {/* AI */}
            <div className="rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-5 backdrop-blur-xl">

              <div className="mb-5 flex items-center gap-2">
                <span className="text-2xl">🤖</span>

                <div>
                  <h2 className="text-xl font-bold text-cyan-300">
                    AI Negotiation
                  </h2>

                  <p className="text-xs text-slate-400">
                    Autonomous Agent Console
                  </p>
                </div>

              </div>

              <div className="space-y-4">

                <div className="rounded-xl border border-cyan-500/20 bg-slate-800/60 p-4">

  <div className="flex items-center justify-between">

    <div>
      <h3 className="font-semibold text-white">
        Agent Alpha
      </h3>

      <p className="text-xs text-slate-400">
        Autonomous Negotiator
      </p>
    </div>

    <div className="flex items-center gap-2">

      <span className="h-2 w-2 rounded-full bg-green-400 animate-ping"></span>

      <span className="text-green-400 text-sm">
        {negotiation?.status ?? "Loading..."}
      </span>

    </div>

  </div>

  <div className="mt-5 space-y-3">

    <div>
      <div className="flex justify-between text-sm">
        <span className="text-slate-400">
          Negotiation Progress
        </span>

        <span className="text-cyan-300">
          {negotiation
  ? `${Math.round(negotiation.confidence * 100)}%`
  : "Loading..."}
        </span>
      </div>

      <div className="mt-2 h-2 rounded-full bg-slate-700">

        <div
  className="h-full rounded-full bg-cyan-400"
  style={{
    width: negotiation
      ? `${negotiation.confidence * 100}%`
      : "0%",
  }}
></div>

      </div>

    </div>

    <div className="text-sm font-mono text-green-400 space-y-1">

      <p>&gt; Winner: {negotiation?.winner ?? "..."}</p>

<p>&gt; Yielding: {negotiation?.yielding_satellite ?? "..."}</p>

<p>&gt; {negotiation?.reason ?? "Loading..."}</p>

    </div>

  </div>

</div>

                <div className="rounded-xl bg-slate-800/60 p-4">

                  <div className="text-sm text-slate-400">
                    Live Logs
                  </div>

                  <div className="mt-3 space-y-2 text-sm">

                    <p className="text-cyan-300">
                      &gt; Initializing...
                    </p>

                    <p className="text-green-400">
                      &gt; Agent Connected
                    </p>

                    <p className="text-yellow-300">
                      &gt; Awaiting Data
                    </p>

                  </div>

                </div>

              </div>

            </div>

            {/* MCP */}

            <div className="mt-6 rounded-2xl border border-cyan-500/20 bg-slate-900/60 p-5 backdrop-blur-xl">

              <h2 className="mb-4 text-xl font-bold text-cyan-300">
                MCP Activity
              </h2>

              <div className="space-y-3">

                <div className="rounded-lg bg-slate-800/60 p-3">

                  <p className="text-sm text-slate-400">
                    Status
                  </p>

                  <p className="mt-1 text-green-400">
                    Connected
                  </p>

                </div>

                <div className="rounded-lg bg-slate-800/60 p-3">

                  <p className="text-sm text-slate-400">
                    Active Requests
                  </p>

                  <p className="mt-1 text-cyan-300">
                    0
                  </p>

                </div>

              </div>

            </div>

          </div>

        </aside>

      </div>

    </div>
  );
}