import './App.css'
import Header from "./components/Header";
import Box from "./components/Box";
import SearchBar from "./components/SearchBar";

function App() {
  return (
    <>
      <div className="flex flex-col w-full justify-center items-center overflow-auto">
        <Header />
        <div className="flex flex-col items-center mt-3 w-full flex-grow mb-30">
          <Box color="white"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
        </div>
        <div className="flex flex-row w-1/2 justify-center mb-2">
          <SearchBar />
        </div>
      </div>
    </>
  );
}

export default App;