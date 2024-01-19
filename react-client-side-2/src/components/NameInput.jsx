import { useContext } from "react";
import { ThemeContext } from "../contexts/ThemeContext";
import { DesignsContext } from "../contexts/DesignsContext";
import { FormInputsContext } from "../contexts/FormInputsContext";


export default function NameInput({ 'name-type': name_type }){
    let name_code = name_type === 'first' ? 'f' : 'l';
    let placeholder = name_type === 'first' ? 'John Smith' : 'Meyer';

    let field_value;
    let setter;
    if(name_type === 'first'){
        let { fname, setFname } = useContext(FormInputsContext);
        field_value = fname;
        setter = setFname;
    }else{
        let { lname, setLname } = useContext(FormInputsContext);
        field_value = lname;
        setter = setLname;
    }

    const capitalize = (string) => string[0].toUpperCase() + string.substring(1);
    

    // initialize and define theme of component by using
    // context
    let style;
    const designs = useContext(DesignsContext);
    const themes = useContext(ThemeContext);
    const { design, theme } = themes;
    
    // sometimes themes context will contain only the design 
    // and not the theme key so check if theme key is in themes
    if('theme' in themes){
        style = designs[design][theme];
    }else{
        style = designs[design];
    }
    
    return (
        <div 
            className={`${name_code}name-container ${design}`} 
            style={style}
        >
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
                value={field_value}
                onChange={(event) => setter(event.target.value)}
            />
        </div>
    );
}