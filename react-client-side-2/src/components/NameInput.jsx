import { useContext, useState } from "react";
import { ThemeContext } from "../contexts/ThemeContext";
import { DesignsContext } from "../contexts/DesignsContext";
import { DesignsContext2 } from '../contexts/DesignsContext2';

export default function NameInput({ 'name-type': name_type }){
    let name, setName = useState("");
    let name_code = name_type === 'first' ? 'f' : 'l';
    let placeholder = name_type === 'first' ? 'John Smith' : 'Meyer';
    const capitalize = (string) => string[0].toUpperCase() + string.substring(1);

    let style;
    let design, theme; 
    const designs = useContext(DesignsContext2);
    const themes = useContext(ThemeContext);
    if('theme' in themes){
        [design, theme] = themes;
        style = designs[design][theme];
        console.log(style);
    }
    else{
        [design] = theme;
        style = designs[design];
        console.log(style);
    }
    
    return (
        <div className={`${name_code}name-container ${design}`} style={style}>
            <label 
                htmlFor="last-name" 
                className={`${name_code}name-label`}
            >{`${capitalize(name_type)} name`}</label>
            <input 
                type="text" 
                name={`${name_type}_name`} 
                id={`${name_type}-name`} 
                className={`${name_code}name-field ${design}`} 
                placeholder={placeholder}
                value={name}
                onChange={(event) => setName(event.target.value)}
            />
        </div>
    );
}