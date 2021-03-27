<template>
  <div class="user" :style="{ backgroundColor: isSpeaking ? '#332940' : '#1F1B24' }">
    <p class="emotion">{{ emoticon }}</p>
    <p class="name">{{ name }}</p>
  </div>
</template>

<script>
export default {
  name: "User",
  props: {
    name: String,
    isSpeaking: Boolean,
    emoticon: String
  },
  data() {
    return {
      
    };
  }
}
</script>

<style lang="scss" scoped>

.emotion {
  font-size: 6em;
}

.name {
  font-family: 'Roboto', sans-serif;  
  color: #03DAC5;
  font-size: 3em;
  position: absolute;
  bottom: 0;
  left: 10px;
  margin: 0 0 0 0;
  opacity: 0.5
}

.user {
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

p {
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -o-user-select: none;
  user-select: none;
}

</style>
