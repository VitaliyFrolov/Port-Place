import { useEffect, useState } from 'react';

export const useScrollTrigger = () => {
    const [scrolled, setScroller] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            if (!scrolled) {
                setScroller(true);
            }
        };

        window.addEventListener('scroll', handleScroll);

        return () => window.removeEventListener('scroll', handleScroll);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return scrolled;
};