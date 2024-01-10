<script>
  import { onMount, onDestroy } from "svelte";
  import Content from "./components/Content.svelte";
  import Correspondence from "./components/Correspondence.svelte";

  import './assets/stylesheets/content.css';
  import './index.css';
  
</script>

<Content>
  <Correspondence/>
</Content>