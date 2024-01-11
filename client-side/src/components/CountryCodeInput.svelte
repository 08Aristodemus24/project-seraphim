<script>
    import { onMount } from "svelte";

    let countries = [];
    let country_code = "";

    const get_country_codes = async () => {
        try{
            const url = 'https://gist.githubusercontent.com/anubhavshrimal/75f6183458db8c453306f93521e93d37/raw/f77e7598a8503f1f70528ae1cbf9f66755698a16/CountryCodes.json';
            const response = await fetch(url);

            if(response.status === 200){
                console.log("retrieval successful");

                const data = await response.json();

                // returned data list consists of dictionaries containing
                // keys name, dial_code, and code e.g. 'Afghanistan', '+93', 'AF'
                countries = [...data];

                // on mount set state of country code to dial code of first country
                country_code = countries[0]['dial_code'];
                // console.table(countries);

            }else{
                console.log(`retrieval unsuccessful. Response status ${response.status} occured`)
            }    

        }catch(error){
            console.log(`Server access denied. Error '${error}' occured`);
        }
    };

    onMount(async () => {
        get_country_codes();
    });
</script>

<div class="country-code-container">
    <label for="country-code" class="country-code-label">Country Code</label>
    <select name="country_code" id="country-code" class="country-code-field" bind:value={country_code}>
        {#each countries as country}
            <option value={country['dial_code']} label={`${country['name']} (${country['dial_code']})`} data-country-name={country['name']} data-country-code={country['code']} data-dial-code={country['dial_code']}></option>
        {/each}
    </select>
</div>