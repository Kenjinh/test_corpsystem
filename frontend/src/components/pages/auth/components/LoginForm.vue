<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';
  
  export default {
    name: 'LoginForm',
    components: {
      NotificationCard
    },
    data() {
      return {
        email: '',
        password: ''
      }
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://localhost:8000/api/auth/', {
            email: this.email,
            password: this.password
          });
          const expiresIn = new Date().getTime() + 5000 * 60 * 60; // 5h
          const token = {
            token: response.data.token,
            expiry: expiresIn,
            UID: response.data.UID
          }
          localStorage.setItem('token', JSON.stringify(token));
          this.$refs.notification.showNotification('success', 'Login efetuado com sucesso');
          this.$router.push('/');
        } catch (error) {
          this.$refs.notification.showNotification('danger', error.response.data.message);
        }
      }
    }
  }
</script>
<template>
  <div class="container">
    <h1>Login</h1>
    <form class="mb-3">
      <div class="mb-3">
        <label for="email" class="from-label">Email</label>
        <input type="text" class="form-control" id="email" v-model="email" placeholder="Email">
      </div>
      <div class="mb-3">
        <label for="password" class="from-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="password" placeholder="Password">
      </div>
    </form>
    <div class="form-footer">
      <button class="btn btn-primary" @click="login">Login</button>
    </div>
    <NotificationCard ref="notification" />
  </div>

</template>
<style>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 50%;
    min-height: 100vh;
  }
</style>