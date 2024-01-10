<script>
    export let name;
</script>

<section id={`${name}-section`}>
    <div class={`${name}-content`}>
        <slot/>
    </div>
</section>