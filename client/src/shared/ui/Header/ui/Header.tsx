'use client'
import { useScrollTrigger } from '@/shared/hooks/useScrollTrigger';
import { Container } from '../../Container';
import { Logo } from '../../Logo';
import styles from './Header.module.scss';

export const Header = () => {
    const scrolled = useScrollTrigger(0);

    return (
        <header
            className={styles.header__wrapper}
            style={scrolled ? {opacity: "1"} : {opacity: "0"}}
        >
            <Container>
                <div className={styles.header}>
                <Logo />
                <nav className={styles.navigation}>
                    <ul className={styles.navigation__list}>
                        <li>
                            О нас
                        </li>
                        <li>
                            Резиденты
                        </li>
                        <li>
                            Игровая зона
                        </li>
                    </ul>
                </nav>
                </div>
            </Container>
        </header>
    );  
};