export default function SearchBar() {
  return (
    <>
      <label className="input w-4/5">
        <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <g
            strokeLinejoin="round"
            strokeLinecap="round"
            strokeWidth="2.5"
            fill="none"
            stroke="currentColor"
          >
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.3-4.3"></path>
          </g>
        </svg>
        <input type="search" required placeholder="Search" />
      </label>
      <button type="submit" className="p-2.5 ml-2.5 text-sm font-medium text-white bg-blue-500 rounded-lg hover:bg-blue-600">
        Submit
      </button>      
    </>
  )
}