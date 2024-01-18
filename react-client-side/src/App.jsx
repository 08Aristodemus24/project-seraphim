import { useState } from 'react';
import Section from './components/Section';
import './App.css';
import { ThemeContext } from './contexts/ThemeContext';
import { DesignsContext } from './contexts/DesignsContext';


function App() {
  return (
    <DesignsContext>      
      <ThemeContext.Provider value={{design: 'light-neomorphic'}}>
        <Section section-name={"data-form"}>

        </Section>
      </ThemeContext.Provider>
    </DesignsContext>
  );
}

export default App;