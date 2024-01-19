import { ThemeContext } from './contexts/ThemeContext';
import { DesignsContext } from './contexts/DesignsContext';
import { DesignsProvider2 } from './contexts/DesignsContext2';

import './App.css'
import NameInput from './components/NameInput';
import Correspondence from './components/Correspondence';



function App() {

  return (
    <DesignsProvider2>
      {/* <DesignsContext.Provider> */}
        <ThemeContext.Provider value={{design: "sharp-minimal", theme: "dark"}}>
          <Correspondence/>
        </ThemeContext.Provider>  
      {/* </DesignsContext.Provider> */}
    </DesignsProvider2>
    
    
  );
}

export default App
