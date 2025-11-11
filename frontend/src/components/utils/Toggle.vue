<template>
  <button
    @click="$emit('update:modelValue', !modelValue)"
    :class="[
      'min-w-10 w-12 h-6 flex items-center rounded-full transition-colors duration-300',
      modelValue ? 'bg-blue-500' : 'bg-gray-300',
      'p-1'
    ]"
  >
    <span
      :class="[
        'w-4 h-4 bg-white rounded-full shadow transform transition-transform duration-300',
        modelValue ? 'translate-x-2 lg:translate-x-3' : '-translate-x-2 lg:-translate-x-3'
      ]"
    ></span>
  </button>
</template>



<script setup>
defineProps({
  modelValue: Boolean
})
defineEmits(['update:modelValue'])
</script>
