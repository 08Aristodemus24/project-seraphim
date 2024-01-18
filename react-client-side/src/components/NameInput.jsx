import { useContext, useState } from "react";
import { ThemeContext } from "../contexts/ThemeContext";

export default function NameInput({ name_type }){
    let name, setName = useState("");
    let name_code = name_type === 'first' ? 'f' : 'l';
    let placeholder = name_type === 'first' ? 'John Smith' : 'Meyer';

    const theme = useContext(ThemeContext);

    return (
        <div className={`${name_code}name-container ${style}`} style={""}>
            <label 
                htmlFor="last-name" 
                className={`${name_code}name-label`}
            >{`${capitalize(name_type)} name`}</label>
            <input 
                type="text" 
                name={`${name_type}_name`} 
                id={`${name_type}-name`} 
                className={`${name_code}name-field ${style}`} 
                placeholder={placeholder}
                value={name}
                onChange={(event) => setName(event.target.value)}
            />
        </div>
    );
}