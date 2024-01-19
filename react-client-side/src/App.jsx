import { useState } from 'react';
import { ThemeContext } from './contexts/ThemeContext';
import { DesignsContext } from './contexts/DesignsContext';

import './App.css';
import Correspondence from './components/Correspondence';

function App() {
  return (
    <DesignsContext>      
      <ThemeContext.Provider value={{design: 'light-neomorphic'}}>
        <Correspondence/>
      </ThemeContext.Provider>
    </DesignsContext>
  );
}

export default App;