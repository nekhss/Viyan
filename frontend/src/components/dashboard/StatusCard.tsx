interface StatusCardProps {
  title: string;
  value: string;
  color?: string;
}

export default function StatusCard({
  title,
  value,
  color = "text-cyan-400",
}: StatusCardProps) {
  return (
    <div className="bg-gray-900 rounded-xl p-6 shadow-lg border border-gray-800">
      <h3 className="text-gray-400 text-sm mb-2">
        {title}
      </h3>

      <p className={`text-3xl font-bold ${color}`}>
        {value}
      </p>
    </div>
  );
}