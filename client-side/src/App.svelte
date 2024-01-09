<script>
  import { onMount, onDestroy } from "svelte";
  import Content from "./components/Content.svelte";
  import Contact from "./components/Contact.svelte";

  import './assets/stylesheets/content.css';
  import './assets/stylesheets/navbar-862-and-up.css';
  import './assets/stylesheets/navbar-862-down.css';
</script>

<Content>
  <Contact slot="contact-section"/>
</Content>