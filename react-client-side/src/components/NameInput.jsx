import { useState } from "react";

export default function NameInput({ name_type, style }){
    let name, setName = useState("");

    return (
        <div className={`${name_code}name-container ${style}`} style={styles[style]?.dark}>
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
            />
        </div>
    );
}

const styles = {
    'sharp-minimal': {
        dark: {
            '--primary-color': "white",
            '--secondary-color': "black",
            '--tertiary-color': "rgba(255, 255, 255, 0.267)"
        },
        light: {
            '--primary-color': "black",
            '--secondary-color': "white",
            '--tertiary-color': "rgba(0, 0, 0, 0.267)"
        }
    },
    'light-neomorphic': {
        '--primary-color': "black",
        '--secondary-color': "rgb(231, 238, 246)",
        '--tertiary-color': "rgba(0, 0, 0, 0.267)",
        '--primary-shadow': "rgba(0, 0, 0, 0.25)",
        '--secondary-shadow': "rgba(255, 255, 255, 0.5)"
    },
    'dark-neomorphic': {
        '--primary-color': "rgb(231, 238, 246)",
        '--secondary-color': "rgb(38,39,43)",
        '--tertiary-color': "rgba(255, 255, 255, 0.267)",
        '--primary-shadow': "rgba(0, 0, 0, 0.25)",
        '--secondary-shadow': "rgba(210, 210, 210, 0.5)"
    }
};