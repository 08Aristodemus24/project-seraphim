<script>
    export let name;
</script>

<section id={`${name}-section`}>
    <div class={`${name}-content`}>
        <slot/>
    </div>
</section>

<style>
    /* LANDING SECTION */
    #data-form-section{
        /* size for each section*/
        /* take into account navbar in data-form section */
        /* min-height: calc(100vh - clamp(3.5rem, 6.5vw, 6.5rem)); */
        min-height: 100vh;
    
        /* position */
        position: relative;

        /* display */
        display: flex;
        justify-content: center;
        align-items: center;
    
        /* design */
        background-color: rgb(231, 238, 246);
        /* border: 2px solid lightseagreen; */
    }
    
    #data-form-section::after{
        /* size */
        width: 100%;
        height: 100%;

        /* position */
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        /* to not affect contents color place pseudo element behind content */
        z-index: -1;

        /* design */
        content: '';
        background-image: url('https://raw.githubusercontent.com/08Aristodemus24/project-seraphim/master/client-side/src/assets/mediafiles/journey-painting-wallpaper.jpg');
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        filter: brightness(75%);
    }

    .data-form-content{
        /* alignment */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        /* design */
        /* outline: 3px solid purple; */
    }
</style>