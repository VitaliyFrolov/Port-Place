export const anchorScroller = (blockId: string) => {
    const block = document.getElementById(blockId);
    if (block) {
        if ('scrollBehavior' in document.documentElement.style) {
            block.scrollIntoView({ behavior: "smooth" });
        } else {
            block.scrollIntoView();
        }
    }
};