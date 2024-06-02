import { useEffect, useState } from "react";

export const useScrollTrigger = (index: number) => {
    const [scrolled, setScroller] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setScroller(window.scrollY > index);
        };

        window.addEventListener('scroll', handleScroll);

        return () => window.removeEventListener('scroll', handleScroll);
    }, [scrolled]);

    return scrolled;
};