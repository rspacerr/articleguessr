interface BoxProps {
  text?: string,
  color: string,
}

export default function Box({ text, color }: BoxProps) {
  return (
    <div className="rounded-box w-3/4 h-16 lg:w-1/2 px-3.5 py-3 mb-2 border-1" style={{borderColor: color}}>
      {text}
    </div>
  );
}