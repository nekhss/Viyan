import { Activity, Clock, Satellite, ShieldCheck } from "lucide-react";
import { useEffect, useState } from "react";

export default function Header() {
  const [time, setTime] = useState("");

  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date();
      setTime(
        now.toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
        })
      );
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  return (
    <header className="h-16 border-b border-cyan-500/10 bg-slate-950/70 backdrop-blur-xl px-6 flex items-center justify-between">

      {/* Left */}
      <div className="flex items-center gap-4">

        <div className="h-11 w-11 rounded-xl bg-cyan-500/10 flex items-center justify-center border border-cyan-500/20">
          <Satellite className="text-cyan-300" size={22} />
        </div>

        <div>
          <h1 className="text-2xl font-bold text-cyan-300">
            VIYAN Mission Control
          </h1>

          <p className="text-xs text-slate-400">
            Autonomous Multi-Agent Orbital Coordination Platform
          </p>
        </div>

      </div>

      {/* Right */}
      <div className="flex items-center gap-8">

        <div className="text-center">
          <p className="text-[11px] uppercase tracking-wider text-slate-500">
            Fleet Status
          </p>

          <div className="flex items-center gap-2 text-green-400 font-semibold">
            <Activity size={16} />
            LIVE
          </div>
        </div>

        <div className="text-center">
          <p className="text-[11px] uppercase tracking-wider text-slate-500">
            System
          </p>

          <div className="flex items-center gap-2 text-cyan-300">
            <ShieldCheck size={16} />
            Secure
          </div>
        </div>

        <div className="text-center">
          <p className="text-[11px] uppercase tracking-wider text-slate-500">
            Local Time
          </p>

          <div className="flex items-center gap-2 text-white">
            <Clock size={16} />
            {time}
          </div>
        </div>

      </div>

    </header>
  );
}