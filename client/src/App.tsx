import './App.css'
import Header from "./components/Header";
import Box from "./components/Box";
import SearchBar from "./components/SearchBar";

function App() {
  const lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam blandit molestie dolor iaculis pretium. Mauris id blandit elit. Praesent id sapien quis elit mollis tincidunt ut pulvinar nulla. Aliquam et efficitur turpis. Mauris vitae elit tincidunt, vestibulum erat nec, tincidunt elit. In rhoncus sed est nec laoreet. Morbi tempor ac massa non volutpat. Vivamus egestas aliquet magna et vulputate. Donec feugiat dolor ut turpis gravida interdum. Quisque dapibus ligula ut cursus finibus.";

  return (
    <>
      <div className="flex flex-col w-full h-screen justify-center items-center overflow-auto">
        <Header />
        <div className="flex flex-col items-center mt-3 w-full flex-grow">
          <Box title="Title of article" text={lorem_ipsum} color="white"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
          <Box color="#6495ED"/>
        </div>
        <div className="flex flex-row w-1/2 justify-center mb-2">
          <SearchBar />
        </div>
        <p className="font-bold mt-3 mb-5">Disclaimer: text filtering is not perfect! Please don't hesitate to let me know about errors.</p>
      </div>
    </>
  );
}

export default App;