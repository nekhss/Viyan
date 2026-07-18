import stars from "../../assets/space/stars.webp";

export default function SpaceBackground() {
  return (
    <>
      {/* Deep Space Gradient */}
      <div className="fixed inset-0 -z-50 bg-gradient-to-br from-[#020617] via-[#071a33] to-black" />

      {/* Star Texture */}
      <div
        className="fixed inset-0 -z-40 opacity-25"
        style={{
          backgroundImage: `url(${stars})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      />

      {/* Blue Glow */}
      <div className="fixed left-1/2 top-1/2 -z-30 h-[700px] w-[700px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-500/10 blur-[180px]" />

      {/* Top Glow */}
      <div className="fixed -top-40 left-1/2 -z-20 h-[400px] w-[400px] -translate-x-1/2 rounded-full bg-blue-500/10 blur-[150px]" />

      {/* Bottom Right Glow */}
      <div className="fixed bottom-0 right-0 -z-20 h-[300px] w-[300px] rounded-full bg-cyan-500/10 blur-[140px]" />
    </>
  );
}