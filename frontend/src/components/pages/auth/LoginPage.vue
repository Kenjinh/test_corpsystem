<script>
  import NotificationCard from '../../general/NotificationCard.vue';
  import LoginForm from './components/LoginForm.vue';
  export default {
    name: 'LoginPage',
    components: {
      NotificationCard,
      LoginForm
    }
  }
</script>
<template>
  <div class="container">
    <LoginForm />
    <NotificationCard ref="notification" />
  </div>
</template>