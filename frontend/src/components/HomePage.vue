// frontend/src/components/HomePage.vue
<template>
  <div>
    <h1 class="mdc-typography--headline1">Welcome to My Evernote App</h1>
    <p class="mdc-typography--body1">
      This is your personal space to organize your thoughts, ideas, and notes.
    </p>
    <mdc-button class="mdc-button--raised" to="/notes">
      View Your Notes
    </mdc-button>
  </div>
</template>

<script>
import { mdcButton } from 'material-components-web/dist/mdc.button';

export default {
  mounted() {
    mdcButton.MDCRipple.attachTo(this.$el.querySelector('.mdc-button'));
  },
};
</script>

<style scoped>
.mdc-button {
  margin-top: 24px;
}
</style>