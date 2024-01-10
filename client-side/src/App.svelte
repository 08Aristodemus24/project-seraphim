<script>
  import { onMount, onDestroy } from "svelte";
  import Content from "./components/Content.svelte";
  import Contact from "./components/Contact.svelte";
  import Section from "./components/Section.svelte";
  import Glass from "./components/Glass.svelte";

  import './assets/stylesheets/content.css';
  
</script>

<Content>
  <!-- <Contact slot="contact-section"/>
  <Section slot="glass-section" name="prompt">
    <Glass/>
  </Section> -->
  <Section slot="landing-section" name="landing"/>
</Content>