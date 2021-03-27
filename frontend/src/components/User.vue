<template>
  <div class="user" :class="speakingBorder">
    <p class="emotion">{{ emoticon }}</p>
    <p class="name">{{ name }}</p>
  </div>
</template>

<script>
export default {
  name: "User",
  props: {
    userData: Object,
  },
  data() {
    return {
      name: this.userData.name,
      isSpeaking: this.userData.isSpeaking,
      emoticon: this.userData.emoticon,
    };
  },
  computed: {
    speakingBorder() {
      return this.isSpeaking ? "speaking" : "silent";
    },
  },
};
</script>

<style lang="scss" scoped>
.speaking {
  background-color: #332940;
}

.silent {
  background-color: #1f1b24;
}

.emotion {
  font-size: 6em;
}

.name {
  font-family: "Roboto", sans-serif;
  color: #03dac5;
  font-size: 3em;
  position: absolute;
  bottom: 0;
  left: 10px;
  margin: 0 0 0 0;
  opacity: 0.5;
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
