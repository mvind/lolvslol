//Home

<template>
  <div>
    <p>Home</p>
  </div>

  <div id='app'>
    <ul>
      <li v-for="item in test">
        {{ item }}
      </li>
    </ul>
  </div>
</template>
