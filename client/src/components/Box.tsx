interface BoxProps {
  title?: string,
  text?: string,
  color: string,
}

export default function Box({ title, text, color }: BoxProps) {
  return (
    <div className="rounded-box w-3/4 h-fit lg:w-1/2 px-3.5 py-3 mb-2 border-1 text-white" style={{borderColor: color}}>
      <h1 className="font-bold">{title}</h1>
      <p className="indent-8 m-1 text-sm">{text}</p>
    </div>
  );
}