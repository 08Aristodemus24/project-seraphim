import { ThemeContext } from './contexts/ThemeContext';
import { DesignsProvider } from './contexts/DesignsContext';

import './App.css'
import NameInput from './components/NameInput';
import Correspondence from './components/Correspondence';



function App() {

  return (
    <DesignsProvider>
      <ThemeContext.Provider value={{design: "light-neomorphic"}}>
        <Correspondence/>
      </ThemeContext.Provider>  
    </DesignsProvider>
    
    
  );
}

export default App
