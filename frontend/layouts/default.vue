<template>
  <div>
    <Header class="container" />
    <Nuxt />
    <Footer class="container" />
  </div>
</template>

<style>
html {
  font-family: source-han-sans-japanese, sans-serif;
  font-size: 14px;
  line-height: 1.5;
  color: #333;
}

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
}

img {
  max-width: 100%;
  height: auto;
}

.container,
.min-container {
  margin: 0 16px;
}

@media (min-width: 768px) {
  .container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 108px;
    box-sizing: border-box;
  }

  .min-container {
    max-width: 984px;
    margin: 0 auto;
    padding: 0 108px;
    box-sizing: border-box;
  }
}

.loading-wrapper {
  text-align: center;
}

.loading {
  display: inline-block;
  width: 1.5rem;
  height: 1.5rem;
  border: 4px solid rgba(9, 133, 81, 0.705);
  border-radius: 50%;
  border-top-color: #158876;
  animation: spin 1s ease-in-out infinite;
}
@keyframes spin {
  to {
    -webkit-transform: rotate(360deg);
  }
}

.field {
  width: 100%;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type='text'],
input[type='email'],
input[type='number'],
input[type='password'],
select,
textarea {
  width: 100%;
  padding: 10px 10px;
  box-sizing: border-box;
  border-radius: 4px;
  border: solid 1px #ccc;
}

button,
a.button {
  outline: none;
  border: none;
  border-radius: 8px;
  background-color: #f5f5f5;
  font-weight: 700;
  font-size: 14px;
  height: 35px;
  cursor: pointer;
  -webkit-transition: 0.25s ease;
  transition: 0.25s ease;
  padding: 6px 12px;
  box-sizing: border-box;
  display: inline-block;
}

button:hover,
a.button:hover {
  background-color: #c3c3c3;
  text-decoration: none;
  color: inherit;
}

a {
  color: inherit;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
  color: #4083ff;
}

.zoom-enter-active,
.zoom-leave-active {
  animation-duration: 0.21s;
  animation-fill-mode: both;
  animation-name: zoom;
}
.zoom-leave-active {
  animation-direction: reverse;
}
@keyframes zoom {
  from {
    opacity: 0;
    transform: scale3d(1.1, 1.1, 1.1);
  }
  100% {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }
}
</style>
