<script>
    export let msg_status;
    export let error_type;
    export let response;

</script>

<div class="alert" class:show={msg_status !== undefined} on:click={(event) => {
    // remove class from alert container to hide it again
    event.target.classList.remove('show');

    // reset msg_status to undefined in case of another submission
    msg_status = undefined;
}}>
    <div class="alert-wrapper">
        {#if msg_status === "success" || msg_status === "failed"}
            <span class="alert-message">Message has been sent with code {response?.status}</span>    
        {:else}
            <span class="alert-message">Submission denied. Error '{error_type?.message}'' occured</span>
        {/if}
    </div>
</div>

<style>
    .alert{
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

    .alert.show{
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
        width: max(10rem, 25%);
        padding: 1rem;

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