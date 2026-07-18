import {
  CheckCircle2,
  Satellite,
  ShieldAlert,
  BrainCircuit,
} from "lucide-react";

const events = [
  {
    title: "SAT-001 entered Low Earth Orbit",
    time: "20:31",
    icon: Satellite,
    color: "text-cyan-400",
  },
  {
    title: "Collision Risk Detected",
    time: "20:34",
    icon: ShieldAlert,
    color: "text-yellow-400",
  },
  {
    title: "AI Negotiation Started",
    time: "20:35",
    icon: BrainCircuit,
    color: "text-purple-400",
  },
  {
    title: "Orbit Successfully Adjusted",
    time: "20:36",
    icon: CheckCircle2,
    color: "text-green-400",
  },
];

export default function Timeline() {
  return (
    <div className="rounded-2xl border border-cyan-500/20 bg-slate-900/60 backdrop-blur-xl p-5">
      <h2 className="text-xl font-bold text-cyan-300 mb-6">
        Mission Timeline
      </h2>

      <div className="space-y-5">
        {events.map((event, index) => {
          const Icon = event.icon;

          return (
            <div key={index} className="flex gap-4">

              <div className="flex flex-col items-center">
                <Icon className={event.color} size={22} />

                {index !== events.length - 1 && (
                  <div className="w-[2px] flex-1 mt-2 bg-cyan-500/20" />
                )}
              </div>

              <div className="flex-1">

                <div className="flex justify-between">

                  <h3 className="font-medium text-white">
                    {event.title}
                  </h3>

                  <span className="text-xs text-slate-500">
                    {event.time}
                  </span>

                </div>

              </div>

            </div>
          );
        })}
      </div>
    </div>
  );
}