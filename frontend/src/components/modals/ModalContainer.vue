<template>
  <transition name="modal-fade">
    <div v-if="store.isModalOpen" class="modal-overlay" @click.self="store.closeModal">
      <div class="modal-content">
        <button class="modal-close-button text-black" @click="store.closeModal">
          &times;
        </button>
        
        <component 
          v-if="store.component"
          :is="store.component" 
          v-bind="store.props" 
        />

      </div>
    </div>
  </transition>
</template>

<script setup>
import { useModalStore } from '@/stores/ModalStore.js';
const store = useModalStore();
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  position: relative;
  min-width: 300px;
}

.modal-close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>