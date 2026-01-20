import './App.css'
import Header from "./components/Header";
import Box from "./components/Box";
import SearchBar from "./components/SearchBar";
import { useEffect, useState } from "react";

type ArticleData = {
  title: string,
  text: string
};

function App() {
  const lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam blandit molestie dolor iaculis pretium. Mauris id blandit elit. Praesent id sapien quis elit mollis tincidunt ut pulvinar nulla. Aliquam et efficitur turpis. Mauris vitae elit tincidunt, vestibulum erat nec, tincidunt elit. In rhoncus sed est nec laoreet. Morbi tempor ac massa non volutpat. Vivamus egestas aliquet magna et vulputate. Donec feugiat dolor ut turpis gravida interdum. Quisque dapibus ligula ut cursus finibus.";
  const [articleData, setArticleData] = useState<ArticleData[]>([]);
  let ignore = false;

  useEffect(() => {
    const getData = async() => {
      const data = await fetch("/api/session", {
        headers:{"Accept":"application/json"}
      });
      const json = await data.json();
      console.log(json);

      setArticleData([
        ...articleData,
        { title: json.title, text: json.sections }
      ]);
    };

    if (!ignore) {
      getData();
    }

    return () => { ignore = true; }
  }, []);

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
        <button className="btn btn-circle btn-error text-white btn-lg absolute bottom-0 right-0 m-5">
          <svg width="800px" height="800px" viewBox="0 0 76.01 76.01" xmlns="http://www.w3.org/2000/svg" version="1.1" baseProfile="full" enable-background="new 0 0 76.01 76.01">
            <path fill="#000000" fill-opacity="1" stroke-width="0.2" stroke-linejoin="round" d="M 50.672,20.5864L 55.4219,25.3364L 55.422,38.0031L 42.7553,38.0031L 38.0053,33.2531L 46.8578,33.2522C 44.6831,30.8224 41.5227,29.2932 38.0052,29.2932C 31.4459,29.2932 26.1285,34.6106 26.1285,41.1699C 26.1285,44.4495 27.4579,47.4187 29.6071,49.5679L 25.6881,53.4869C 22.5359,50.3347 20.5862,45.9799 20.5862,41.1698C 20.5862,31.5494 28.385,23.7507 38.0053,23.7507C 42.9966,23.7507 47.4975,25.8499 50.6734,29.2137L 50.672,20.5864 Z "/>
          </svg>
        </button>
        <p className="font-bold mt-3 mb-5">Disclaimer: text filtering is not perfect! Please don't hesitate to let me know about errors.</p>
      </div>
    </>
  );
}

export default App;