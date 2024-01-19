import { ThemeContext } from './contexts/ThemeContext';
import { DesignsContext } from './contexts/DesignsContext';

import Correspondence from './components/Correspondence';

import './App.css';

function App() {
  return (
    // <DesignsContext>      
    //   <ThemeContext.Provider value={{design: 'light-neomorphic'}}>
        <Correspondence></Correspondence>
    //   </ThemeContext.Provider>
    // </DesignsContext>
  );
}

export default App;