<template>
  <div v-if="notification" :class="['notification', notification.type]">
    {{ notification.message }}
    <button class="btn" @click="closeNotification">Fechar</button>
  </div>
</template>

<script>
export default {
  name: 'Notification',
  data() {
    return {
      notification: null,
    };
  },
  methods: {
    showNotification(type, message) {
      this.notification = { type, message };
      setTimeout(() => {
        this.closeNotification();
      }, 5000);
    },
    closeNotification() {
      this.notification = null;
    },
  },
};
</script>

<style>
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 10px;
  border-radius: 5px;
  z-index: 1000;
}

.success {
  background-color: #4caf50;
  color: white;
}

.error {
  background-color: #f44336;
  color: white;
}
</style>
