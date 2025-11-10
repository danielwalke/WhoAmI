import { defineStore } from 'pinia'
import { shallowRef, ref } from 'vue'

export const useModalStore = defineStore('modal', {
  state: () => ({ isModalOpen: false, component: shallowRef(null), props: {} }),
  getters: {
    getIsModalOpen: (state) => state.isModalOpen
  },
  actions: {
    openModal(componentToLoad, componentProps = {}) {
        this.component = componentToLoad;
        this.props = componentProps;
        this.isModalOpen = true;
  },
  closeModal() {
      this.isModalOpen = false;
      this.component = null;
      this.props = {};
    }
}
})