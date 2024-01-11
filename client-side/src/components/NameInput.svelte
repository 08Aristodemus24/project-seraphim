<script>
    export let name_type;
    let name_code = name_type === 'first' ? 'f' : 'l';
    let placeholder = name_type === 'first' ? 'John Smith' : 'Meyer';
    let name;

    const capitalize = (string) => string[0].toUpperCase() + string.substring(1);
</script>

<div class={`${name_code}name-container`}>
    <label for="last-name" class={`${name_code}name-label`}>{`${capitalize(name_type)} name`}</label>
    <input type="text" name={`${name_type}_name`} id={`${name_type}-name`} class={`${name_code}name-field`} placeholder={placeholder} bind:value={name}/>
</div>