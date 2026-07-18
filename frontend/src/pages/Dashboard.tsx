import OrbitView from "../components/orbit/OrbitView";
import Timeline from "../components/layout/Timeline";

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <OrbitView />
      <Timeline />
    </div>
  );
}