(() => {
  const refs = {
    openModalBtn: document.querySelector("[data-modal-open]"),
    openModalBtnFixed: document.querySelector("[data-modal-open-fixed]"),
    closeModalBtn: document.querySelector("[data-modal-close]"),
    modal: document.querySelector("[data-modal]"),
    backdrop: document.querySelector(".backdrop"),
  };

  if (refs.openModalBtn)
    refs.openModalBtn.addEventListener("click", toggleModal);
  if (refs.openModalBtnFixed)
    refs.openModalBtnFixed.addEventListener("click", toggleModal);
  if (refs.closeModalBtn)
    refs.closeModalBtn.addEventListener("click", toggleModal);
  if (refs.closeModalBtn)
    refs.backdrop.addEventListener("click", backdropClick);

  function toggleModal() {
    refs.modal.classList.toggle("is-hidden");
  }

  function backdropClick(e) {
    if (e.target !== e.currentTarget) return;
    refs.modal.classList.toggle("is-hidden");
  }
})();
