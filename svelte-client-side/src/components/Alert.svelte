<script>
    export let msg_status;
    export let error_type;
    export let response;

</script>



<style>
    .alert-container{
        /* position */
        position: fixed;
        inset: 0;
        margin: auto;
        z-index: 20;

        /* design */
        opacity: 0%;
        visibility: hidden;
        background-color: rgba(0, 0, 0, 0.377);

        /* transition */
        transition: 
            opacity 0.25s ease-in-out,
            visibility 0.25s ease-in-out;
    }

    .alert-container.show{
        opacity: 100%;
        visibility: visible;
    }

    .alert-wrapper{
        /* position */
        position: absolute;
        top: 0;
        inset-inline: 0;
        margin-inline: auto;

        /* display */
        display: flex;
        justify-content: center;
        align-items: center;

        /* size */
        height: 12.5%;
        width: 25%;

        /* design */
        color: black;
        text-align: center;
        font-size: clamp(10px, 1vw, 1rem);
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
        background-color: white;
        /* outline: 1px solid; */
    }
</style>